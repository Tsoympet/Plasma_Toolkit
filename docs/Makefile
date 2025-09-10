
SPHINXBUILD?=sphinx-build
SOURCEDIR=.
BUILDDIR=_build
.PHONY: html latexpdf clean
html:
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" -W --keep-going -n
latexpdf:
	$(SPHINXBUILD) -b latex "$(SOURCEDIR)" "$(BUILDDIR)/latex" -W --keep-going -n
	$(MAKE) -C "$(BUILDDIR)/latex" all-pdf
clean:
	rm -rf "$(BUILDDIR)"
