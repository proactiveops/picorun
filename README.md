# PicoRun

PicoRun is a small collection of classes used by the default PicoFun 
implementation at runtime. These shared runtime classes help keep the 
code simple.

Spinning PicoRun out into this package prevents lots of duplication
and bloated deployment packages. PicoRun should be included in a common
lambda layer so the lambda functions stay small. Example uses of PicoRun 
can be found in the [PicoFun 
examples](https://github.com/proactiveops/picofun/tree/main/examples).

For more information about PicoFun, check out the [project on 
GitHub](https://github.com/proactiveops/picofun).