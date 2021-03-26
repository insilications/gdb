#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : gdb
Version  : 10.1
Release  : 277
URL      : file:///aot/build/clearlinux/packages/gdb/gdb-10.1.tar.xz
Source0  : file:///aot/build/clearlinux/packages/gdb/gdb-10.1.tar.xz
Summary  : zlib compression library
Group    : Development/Tools
License  : GFDL-1.1 GPL-1.0+ GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-2.0+ LGPL-2.1 Public-Domain
Requires: gdb-bin = %{version}-%{release}
Requires: gdb-data = %{version}-%{release}
Requires: gdb-info = %{version}-%{release}
Requires: gdb-locales = %{version}-%{release}
Requires: gdb-man = %{version}-%{release}
BuildRequires : autoconf
BuildRequires : binutils-dev
BuildRequires : bison
BuildRequires : buildreq-golang
BuildRequires : dejagnu
BuildRequires : expat-dev
BuildRequires : expat-staticdev
BuildRequires : expect
BuildRequires : flex
BuildRequires : gcc-libgcc32
BuildRequires : gettext
BuildRequires : gfortran
BuildRequires : glibc-dev32
BuildRequires : glibc-locale
BuildRequires : glibc-staticdev
BuildRequires : gmp
BuildRequires : gmp-dev
BuildRequires : libxslt-bin
BuildRequires : mpfr
BuildRequires : mpfr-dev
BuildRequires : mpfr-lib
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(zlib)
BuildRequires : processor-trace-dev
BuildRequires : procps-ng
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : sed
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains various GNU compilers, assemblers, linkers,
debuggers, etc., plus their support routines, definitions, and documentation.

%package bin
Summary: bin components for the gdb package.
Group: Binaries
Requires: gdb-data = %{version}-%{release}

%description bin
bin components for the gdb package.


%package data
Summary: data components for the gdb package.
Group: Data

%description data
data components for the gdb package.


%package dev
Summary: dev components for the gdb package.
Group: Development
Requires: gdb-bin = %{version}-%{release}
Requires: gdb-data = %{version}-%{release}
Provides: gdb-devel = %{version}-%{release}
Requires: gdb = %{version}-%{release}

%description dev
dev components for the gdb package.


%package info
Summary: info components for the gdb package.
Group: Default

%description info
info components for the gdb package.


%package locales
Summary: locales components for the gdb package.
Group: Default

%description locales
locales components for the gdb package.


%package man
Summary: man components for the gdb package.
Group: Default

%description man
man components for the gdb package.


%package staticdev
Summary: staticdev components for the gdb package.
Group: Default
Requires: gdb-dev = %{version}-%{release}

%description staticdev
staticdev components for the gdb package.


%prep
%setup -q -n gdb-10.1
cd %{_builddir}/gdb-10.1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616754904
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g3 -O3 -Wl,--no-as-needed --param=lto-max-streaming-parallelism=16 -fgraphite-identity -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16"
#
export CXXFLAGS="-g3 -O3 -Wl,--no-as-needed --param=lto-max-streaming-parallelism=16 -fgraphite-identity -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16"
#
export LDFLAGS="-g3 -O3 -Wl,--no-as-needed -Wl,--whole-archive /usr/lib64/haswell/libpython3.9.so -Wl,--no-whole-archive --param=lto-max-streaming-parallelism=16 -fgraphite-identity -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
unset CCACHE_DISABLE
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags1 end
%configure --enable-static \
--enable-targets=%{_arch}-unknown-linux-gnu \
--target=%{_arch}-generic-linux-gnu \
--enable-tui \
--disable-binutils \
--disable-ld \
--disable-gold \
--disable-gas \
--disable-sim \
--disable-gprof \
--with-intel-pt \
--with-separate-debug-dir=/usr/lib/debug \
--enable-plugins \
--with-system-zlib \
--with-python=yes \
--with-python=/usr/bin/python3 \
--disable-rpath \
PYTHON=/usr/bin/python3
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1616754904
rm -rf %{buildroot}
%make_install
%find_lang bfd
%find_lang opcodes
## Remove excluded files
rm -f %{buildroot}/usr/share/info/bfd.info
rm -f %{buildroot}/usr/include/bfd.h
rm -f %{buildroot}/usr/include/bfd_stdint.h
rm -f %{buildroot}/usr/include/bfdlink.h
rm -f %{buildroot}/usr/include/ctf-api.h

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gcore
/usr/bin/gdb
/usr/bin/gdb-add-index
/usr/bin/gdbserver

%files data
%defattr(-,root,root,-)
/usr/share/gdb/python/gdb/FrameDecorator.py
/usr/share/gdb/python/gdb/FrameIterator.py
/usr/share/gdb/python/gdb/__init__.py
/usr/share/gdb/python/gdb/command/__init__.py
/usr/share/gdb/python/gdb/command/explore.py
/usr/share/gdb/python/gdb/command/frame_filters.py
/usr/share/gdb/python/gdb/command/pretty_printers.py
/usr/share/gdb/python/gdb/command/prompt.py
/usr/share/gdb/python/gdb/command/type_printers.py
/usr/share/gdb/python/gdb/command/unwinders.py
/usr/share/gdb/python/gdb/command/xmethods.py
/usr/share/gdb/python/gdb/frames.py
/usr/share/gdb/python/gdb/function/__init__.py
/usr/share/gdb/python/gdb/function/as_string.py
/usr/share/gdb/python/gdb/function/caller_is.py
/usr/share/gdb/python/gdb/function/strfns.py
/usr/share/gdb/python/gdb/printer/__init__.py
/usr/share/gdb/python/gdb/printer/bound_registers.py
/usr/share/gdb/python/gdb/printing.py
/usr/share/gdb/python/gdb/prompt.py
/usr/share/gdb/python/gdb/types.py
/usr/share/gdb/python/gdb/unwinder.py
/usr/share/gdb/python/gdb/xmethod.py
/usr/share/gdb/syscalls/aarch64-linux.xml
/usr/share/gdb/syscalls/amd64-linux.xml
/usr/share/gdb/syscalls/arm-linux.xml
/usr/share/gdb/syscalls/freebsd.xml
/usr/share/gdb/syscalls/gdb-syscalls.dtd
/usr/share/gdb/syscalls/i386-linux.xml
/usr/share/gdb/syscalls/mips-n32-linux.xml
/usr/share/gdb/syscalls/mips-n64-linux.xml
/usr/share/gdb/syscalls/mips-o32-linux.xml
/usr/share/gdb/syscalls/netbsd.xml
/usr/share/gdb/syscalls/ppc-linux.xml
/usr/share/gdb/syscalls/ppc64-linux.xml
/usr/share/gdb/syscalls/s390-linux.xml
/usr/share/gdb/syscalls/s390x-linux.xml
/usr/share/gdb/syscalls/sparc-linux.xml
/usr/share/gdb/syscalls/sparc64-linux.xml
/usr/share/gdb/system-gdbinit/elinos.py
/usr/share/gdb/system-gdbinit/wrs-linux.py

%files dev
%defattr(-,root,root,-)
/usr/include/ansidecl.h
/usr/include/ctf.h
/usr/include/diagnostics.h
/usr/include/dis-asm.h
/usr/include/gdb/jit-reader.h
/usr/include/plugin-api.h
/usr/include/symcat.h
/usr/lib64/libinproctrace.so

%files info
%defattr(0644,root,root,0755)
/usr/share/info/annotate.info
/usr/share/info/gdb.info
/usr/share/info/gdb.info-1
/usr/share/info/gdb.info-2
/usr/share/info/gdb.info-3
/usr/share/info/gdb.info-4
/usr/share/info/gdb.info-5
/usr/share/info/gdb.info-6
/usr/share/info/gdb.info-7
/usr/share/info/gdb.info-8
/usr/share/info/stabs.info

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gcore.1
/usr/share/man/man1/gdb-add-index.1
/usr/share/man/man1/gdb.1
/usr/share/man/man1/gdbserver.1
/usr/share/man/man5/gdbinit.5

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libbfd.a
/usr/lib64/libctf-nobfd.a
/usr/lib64/libctf.a
/usr/lib64/libopcodes.a

%files locales -f bfd.lang -f opcodes.lang
%defattr(-,root,root,-)

