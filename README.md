# Rhishab's Table
<img align="right" width="400" src="https://github.com/stephansmit/RishabsTable/blob/master/table.png">

Table as requested by Rishabh
## Requirements

The following packages are required
~~~
pip3 install --upgrade numpy pip
pip3 install CoolProp pandas matplotlib
~~~

Or use Singularity, see below.

## Use
Locally
~~~~
python3 make_table.py
~~~~

Run using [Singularity](https://sylabs.io/singularity/)
~~~~
singularity pull shub://stephansmit/gmsh_containers
singularity exec gmsh_containers_latest.sif python3 make_table.py
~~~~
