import os
import pandas as pd
import pm4py
from pm4py.algo.discovery.correlation_mining import algorithm as correlation_miner
from pm4py.visualization.dfg import visualizer as dfg_visualizer
from pm4py.algo.conformance.alignments.process_tree.util import search_graph_pt_frequency_annotation
from pm4py.visualization.process_tree import visualizer as pt_visualizer
from pm4py.objects.petri_net.utils import reachability_graph
from pm4py.visualization.transition_system import visualizer as ts_visualizer
from pm4py.algo.transformation.log_to_features.util import locally_linear_embedding
from pm4py.visualization.graphs import visualizer
from pm4py.algo.filtering.log.attributes import attributes_filter
from pm4py.visualization.graphs import visualizer as graphs_visualizer
from pm4py.algo.evaluation.generalization import algorithm as generalization_evaluator
from pm4py.algo.evaluation.simplicity import algorithm as simplicity_evaluator
from pm4py.statistics.variants.log import get as variants_module


os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'


dataframe = pd.read_csv('eventlog.csv', nrows=100)
dataframe = dataframe.drop(['Unnamed: 0'], axis=1)

dataframe = pm4py.format_dataframe(dataframe, case_id='CaseID', activity_key='Activity', timestamp_key='Timestamp')

event_stream = pm4py.convert_to_event_stream(dataframe)
event_log = pm4py.convert_to_event_log(dataframe)

activities_freq = dict(dataframe["concept:name"].value_counts())
net, im, fm = pm4py.discover_petri_net_alpha(event_log)

print(activities_freq)

def correlationMiner():
    frequency_dfg, performance_dfg = correlation_miner.apply(dataframe, parameters={
        correlation_miner.Variants.CLASSIC.value.Parameters.ACTIVITY_KEY: "concept:name",
        correlation_miner.Variants.CLASSIC.value.Parameters.TIMESTAMP_KEY: "time:timestamp"})
    gviz_freq = dfg_visualizer.apply(frequency_dfg, variant=dfg_visualizer.Variants.FREQUENCY, activities_count=activities_freq, parameters={"format": "svg"})
    gviz_perf = dfg_visualizer.apply(performance_dfg, variant=dfg_visualizer.Variants.PERFORMANCE, activities_count=activities_freq, parameters={"format": "svg"})
    dfg_visualizer.view(gviz_freq)
    dfg_visualizer.view(gviz_perf)


def frequencyAnnotationOfAProcessTree():
    tree = pm4py.convert_to_process_tree(net, im, fm)
    print(tree)
    aligned_traces = pm4py.conformance_diagnostics_alignments(event_log, tree)
    tree = search_graph_pt_frequency_annotation.apply(tree, aligned_traces)
    gviz = pt_visualizer.apply(tree, parameters={"format": "svg"}, variant=pt_visualizer.Variants.FREQUENCY_ANNOTATION)
    pt_visualizer.view(gviz)


def reachabilityGraph():
    ts = reachability_graph.construct_reachability_graph(net, im)
    gviz = ts_visualizer.apply(ts, parameters={ts_visualizer.Variants.VIEW_BASED.value.Parameters.FORMAT: "svg"})
    ts_visualizer.view(gviz)


def evolutionOfFeatures():
    x, y = locally_linear_embedding.apply(event_log)
    gviz = visualizer.apply(x, y, variant=visualizer.Variants.DATES,
                            parameters={"title": "Locally Linear Embedding", "format": "svg", "y_axis": "Intensity"})
    visualizer.view(gviz)


def distributionOfEventsOverTime():
    x, y = attributes_filter.get_kde_date_attribute(event_log, attribute="time:timestamp")
    gviz = graphs_visualizer.apply_plot(x, y, variant=graphs_visualizer.Variants.DATES)
    graphs_visualizer.view(gviz)


def eventsDistribution():
    pm4py.view_events_distribution_graph(event_log, distr_type="hours", format="svg")


def logModelEvaluation():
    # Precision
    prec = pm4py.precision_token_based_replay(event_log, net, im, fm)
    print(prec)

    # Generalization
    gen = generalization_evaluator.apply(event_log, net, im, fm)
    print(gen)

    # Simplicity
    simp = simplicity_evaluator.apply(net)
    print(simp)

    language = variants_module.get_language(event_log)
    print(language)


def monteCarloSimulation():
    dfg_perf, sa, ea = pm4py.discover_performance_dfg(event_log)
    ratio = pm4py.get_rework_cases_per_activity(event_log)
    print(ratio)
    net, im, fm = pm4py.convert_to_petri_net(dfg_perf, sa, ea)
    from pm4py.algo.simulation.montecarlo import algorithm as montecarlo_simulation
    from pm4py.algo.conformance.tokenreplay.algorithm import Variants

    parameters = {}
    parameters[
        montecarlo_simulation.Variants.PETRI_SEMAPH_FIFO.value.Parameters.TOKEN_REPLAY_VARIANT] = Variants.BACKWARDS
    parameters[montecarlo_simulation.Variants.PETRI_SEMAPH_FIFO.value.Parameters.PARAM_CASE_ARRIVAL_RATIO] = 10800
    simulated_log, res = montecarlo_simulation.apply(event_log, net, im, fm, parameters=parameters)

    print(simulated_log)
    print(res)


#correlationMiner()
# frequencyAnnotationOfAProcessTree()
# reachabilityGraph()
# evolutionOfFeatures()
# distributionOfEventsOverTime()
# eventsDistribution()
# logModelEvaluation()
# monteCarloSimulation()
