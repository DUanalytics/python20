#Topic:
#-----------------------------
#libraries



import os
from pm4py.objects.log.importer.xes import factory as xes_importer
log = xes_importer.import_log(os.path.join("pmdata/","running-example.xes"))
log
from pm4py.algo.discovery.alpha import factory as alpha_miner
net, initial_marking, final_marking = alpha_miner.apply(log)
net



#direct flow
import os
from pm4py.objects.log.importer.xes import factory as xes_importer
log = xes_importer.import_log(os.path.join("pmdata/running-example.xes"))

from pm4py.algo.discovery.dfg import factory as dfg_factory
dfg = dfg_factory.apply(log)

from pm4py.visualization.dfg import factory as dfg_vis_factory
gviz = dfg_vis_factory.apply(dfg, log=log, variant="frequency")
dfg_vis_factory.view(gviz)


#decoration
from pm4py.algo.discovery.dfg import factory as dfg_factory
from pm4py.visualization.dfg import factory as dfg_vis_factory

dfg = dfg_factory.apply(log, variant="performance")
gviz = dfg_vis_factory.apply(dfg, log=log, variant="performance")
dfg_vis_factory.view(gviz)
