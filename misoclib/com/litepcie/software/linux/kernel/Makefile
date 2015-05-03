# Makefile for kernel module
MODULE := litepcie.c
DEV_NAME := litepcie0

# Comment/uncomment the following line to disable/enable debugging
#DEBUG:=y

ccflags-$(DEBUG) += -DDEBUG

ifneq ($(KERNELRELEASE),)
	obj-m := $(MODULE:.c=.o)
else
	KERNELDIR ?= /lib/modules/$(shell uname -r)/build
	PWD := $(shell pwd)
endif

KBUILDBASE =+ $(MAKE) -C $(KERNELDIR) M=$(PWD)

define insmod
$(shell $(shell echo `which insmod`) $1)
endef
define rmmod
$(shell $(shell echo `which rmmod`) $1)
endef

.PHONY: rmmod clean

all: litepcie.ko

litepcie.ko:
	$(KBUILDBASE) modules

insmod: litepcie.ko
	$(call insmod, $(MOULE:.c=.ko))

rmmod:
	$(call rmmod, $(MODULE:.c=))

clean:
	$(KBUILDBASE) clean
