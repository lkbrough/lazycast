SUBDIRS := $(filter $(wildcard images/*.png),$(wildcard */.))

all: $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@

.PHONY: all $(SUBDIRS)
