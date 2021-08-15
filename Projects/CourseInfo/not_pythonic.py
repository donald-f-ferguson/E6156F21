
oDesign.ChangeProperty(
    ["NAME:AllTabs",
        ["NAME:HfssTab",
            ["NAME:PropServers", "AnalysisSetup:Setup8"],
                ["NAME:ChangedProps", [ "NAME:Solution Freq", "MustBeInt:=", False, "Value:=", "500MHz"]]]])



hfss = hfss(....)
prof = hfss.getProject(....)
analysis = proj.analysis['Setup8']
analysis.solution_frequency = 500
