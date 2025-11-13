import nbformat, glob

# Recursively process all notebooks in current folder
for f in glob.glob("**/*.ipynb", recursive=True):
    nb = nbformat.read(f, as_version=4)
    changed = False

    # Remove top-level widget metadata
    if 'widgets' in nb.metadata:
        del nb.metadata['widgets']
        changed = True

    # Remove cell-level widget metadata
    for cell in nb.cells:
        if 'metadata' in cell and 'widgets' in cell['metadata']:
            del cell['metadata']['widgets']
            changed = True

    if changed:
        nbformat.write(nb, f)
        print(f"Cleaned widgets from {f}")
    else:
        print(f"No widget metadata in {f}")
