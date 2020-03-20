#pm in python

#pip install graphviz
#https://pypi.org/project/graphviz/
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'
from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.objects.log.importer.xes import factory as importer
from pm4py.visualization.petrinet import factory as visualizer
log = importer.apply('pmdata/running-example.xes')
net, initial_marking, final_marking = alpha_miner.apply(log)
gviz = visualizer.apply(net, initial_marking, final_marking)
visualizer.view(gviz)

print(log[0]) #prints the first trace of the log
print(log[0][0]) #prints the first event of the first trace of the given log

from pm4py.objects.log.exporter.xes import factory as xes_exporter
xes_exporter.export_log(log, "data/exportedLog.xes")

#https://pm4py.fit.fraunhofer.de/documentation#importing

import os
from pm4py.objects.log.importer.csv import factory as csv_importer
event_stream = csv_importer.import_event_stream( os.path.join("pmdata/", "running-example.csv") )
event_stream

from pm4py.objects.conversion.log import factory as conversion_factory
log = conversion_factory.apply(event_stream)

import os
from pm4py.objects.log.adapters.pandas import csv_import_adapter
from pm4py.objects.conversion.log import factory as conversion_factory
dataframe = csv_import_adapter.import_dataframe_from_path( os.path.join("pmdata/","running-example.csv"), sep=',')
dataframe
dataframe.head()
dataframe.summary()
log = conversion_factory.apply(dataframe)


from pm4py.objects.log.exporter.csv import factory as csv_exporter
csv_exporter.export(event_stream, "data/outputFile1.csv")


#sorting
log
from pm4py.objects.log.util import sorting
log = sorting.sort_timestamp(log)
log
from pm4py.objects.log.util import sorting
sorted_log = sorting.sort_lambda(log, lambda x: x.attributes["concept:name"], reverse=False)
sorted_log

#sampling
from pm4py.objects.log.util import sampling
sampled_log = sampling.sample(log, n=50)
sampled_log
#links
#http://www.processmining.org/event_logs_and_models_used_in_book