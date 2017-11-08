# pycog3

Simple, opinionated library for building Cog commands in Python3.

## Usage

pycog3 combines information available in the Cog runtime environment
with assumptions about Python project structure to simplify command
development.

pycog3 includes a driver executable, [bin/cog-command](https://github.com/cog-bundles/pycog3/blob/master/bin/cog-command), which dynamically
imports, instantiates, and runs Python command code based on the
values of `$COG_BUNDLE` and `$COG_COMMAND`.

`cog-command`'s magic requires that Python projects follow a strict
directory layout:

```
<bundle_name>
  |
  |-- <bundle_name>
       |-- __init__.py
       |-- commands
           |
           |-- __init__.py
           |-- <command1>.py
           |-- <command2>.py

```

pycog3 also supports multi-level by using the `-` field separator in the command name. 
For example, defining:
 * `command1` - maps to `!command1`
 * `level1-command` - maps to `!level1-command`
 * `level1-level2-command` - maps to `!level1-level2-command`
 * `level1-...-...-levelN-command` - maps to `!level1-...-...-levelN-command`
 

```
<bundle_name>
  |
  |-- <bundle_name>
       |-- __init__.py
       |-- commands
           |
           |-- __init__.py
           |-- <command1>.py
           |-- <level1>
                |
                |-- __init__.py
                |-- <command>.py
                |-- <level2>
                |    |
                |    |-- <command>.py
                |
                |-- <...>
                     |
                     |-- <...>
                         | 
                         | -- <levelN>
                              |
                              |-- <command>.py           
```


## Examples

See the [cog-bundles/statuspage](https://github.com/cog-bundles/statuspage) repository for an example of this library in action.

If you're interested in the multi-level usage, check the cog-bundle [pi-bundle](https://github.com/pan-net-security/pi-bundle).

## Installation

Add this line to your application's setup.py or requirements.txt:

```
pycog3>=0.1.28
```

## TODO

- Add [Cog service](http://docs.operable.io/docs/services) support
- Add transparent accumulation support a la [cog-bundles/cog-rb](https://github.com/cog-bundles/cog-rb)
