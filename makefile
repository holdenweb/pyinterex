OBJDIR := pp
SRCDIR := src
OBJS := $(addprefix $(OBJDIR)/,test1.pp execute.pp)

$(OBJDIR)/%.pp : $(SRCDIR)/%.py
	python execute.py $< > $@

all: $(OBJS)

#$(OBJS): | $(OBJDIR)

$(OBJDIR):
	mkdir $(OBJDIR)

