SUBDIRS := $(filter %.png,$(wildcard */.))

all: $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@

.PHONY: all $(SUBDIRS)
