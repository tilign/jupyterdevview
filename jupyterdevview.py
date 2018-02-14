def _custom_for_suffix(suffix):
    import subprocess
    import shutil
    import os
    import sys
    custom_dir = os.path.join(subprocess.check_output('jupyter --config-dir',shell=True).strip(), 'custom')
    custom_css_path = os.path.join(custom_dir, 'custom.css')
    custom_css_sources_path = os.path.join(sys.prefix,'share/jupyterdevview/custom.css')
    if not os.path.exists(custom_dir):
        os.makedirs(custom_dir)
    shutil.copy('{}.{}'.format(custom_css_sources_path, suffix), custom_css_path)

def dev_view():
    """Switch jupyter to dev view"""
    _custom_for_suffix('dev')

def notebook_view():
    """Switch jupyter to notebook view"""
    _custom_for_suffix('notebook')
