import view
import imp
import exp

def start():
    type = view.get_type()
    if type == 1:
        imp.import_data()
    elif type == 2:
        out = view.get_out()
        if out == 1:
            exp.export_data()
        elif out == 2:
            exp.exp_name()
