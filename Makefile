all:	squashfsbroadcom squashfsbroadcom40 squashfsralink squashfsrealtek squashfsatheros squashfsatheros2 squashfsatheros40 squashfsopenwrtold squashfsddwrt squashfs43 cramfsunpack claritysimg2img

squashfsbroadcom:
	cd squashfs-broadcom; make

squashfsbroadcom40:
	cd squashfs-broadcom40; make

squashfsralink:
	cd squashfs-ralink; make

squashfsrealtek:
	cd squashfs-realtek/squashfs-tools; make

#squashfsrealtek2:
#	cd squashfs-realtek2/squashfs-2.1-r2; make

squashfsatheros:
	cd squashfs-atheros; make

squashfsatheros2:
	cd squashfs-atheros2; make

squashfsatheros40:
	cd squashfs-atheros4.0/squashfs-tools; make

squashfsopenwrtold:
	cd squashfs-openwrt; make

squashfsddwrt:
	cd squashfs-ddwrt; make

squashfs43:
	cd squashfs4.3/squashfs-tools; make

cramfsunpack:
	cd cramfs; ./configure --without-ncurses; make
	mv cramfs/disk-utils/fsck.cramfs cramfs/disk-utils/clarity-fsck.cramfs

claritysimg2img:
	cd simg2img; make
