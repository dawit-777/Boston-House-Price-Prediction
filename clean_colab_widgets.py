import nbformat, pathlib

for path in pathlib.Path(".").rglob("*.ipynb"):
    nb = nbformat.read(str(path), as_version=4)
    changed = False

    # Remove top-level widgets metadata
    if 'widgets' in nb.metadata:
        del nb.metadata['widgets']
        changed = True

    # Remove cell-level widgets, including outputs
    for cell in nb.cells:
        if 'metadata' in cell and 'widgets' in cell['metadata']:
            del cell['metadata']['widgets']
            changed = True
        if 'outputs' in cell:
            for output in cell['outputs']:
                if 'metadata' in output and 'widgets' in output['metadata']:
                    del output['metadata']['widgets']
                    changed = True

    if changed:
        nbformat.write(nb, str(path))
        print(f"Cleaned widgets from {path}")
    else:
        print(f"No widget metadata in {path}")
