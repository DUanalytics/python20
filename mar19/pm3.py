#Topic:
#-----------------------------
#libraries

from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.objects.log.importer.xes import factory as importer
from pm4py.visualization.petrinet import factory as visualizer
from pm4py.objects.log.importer.csv import factory as csv_importer
event_stream = csv_importer.import_event_stream( os.path.join("pmdata/", "running-example.csv") )
event_stream

event_stream_length = len(event_stream)
print(event_stream_length)
for event in event_stream:    print(event)

from pm4py.objects.conversion.log import factory as conversion_factory

log = conversion_factory.apply(event_stream)

from pm4py.objects.log.exporter.csv import factory as csv_exporter

csv_exporter.export(event_stream, "data/outputFile1.csv")

#log = importer.apply('pmdata/running-example.xes')
net, initial_marking, final_marking = alpha_miner.apply(log)
gviz = visualizer.apply(net, initial_marking, final_marking)
visualizer.view(gviz)