Summary:	A program for handling multimedia mail using the mailcap file
Name:		metamail
Version:	2.7
Release:	12mdk
License:	Distributable
Group:		Networking/Mail
Source0:	ftp://thumper.bellcore.com/pub/nsp/metamail/mm2.7.tar.bz2
Patch0:		mm-2.7-make.patch
Patch1:		mm-2.7-fonts.patch
Patch2:		mm-2.7-glibc.patch
Patch3:		mm-2.7-csh.patch
Patch4:		mm-2.7-uudecode.patch
Patch5:		mm-2.7-sunquote.patch
Patch7:		mm-2.7-ohnonotagain.patch
Patch8:		mm-2.7-arghhh.patch
Patch9:		mm-2.7-sml.patch
Patch10:	metamail-2.7-nl.patch
Patch11:	mm-2.7-linux.patch
Patch12:	metamail-2.7-vulns.patch
Patch13:	mm2.7-gcc3.4-fix.patch
Patch14:	metamail-2.7-boundary_crash.patch
Patch15:	mm2.7-gcc4.patch

Requires:	mktemp sharutils csh
BuildRequires:	termcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	XFree86

%description
Metamail is a system for handling multimedia mail, using the mailcap
file.  Metamail reads the mailcap file, which tells Metamail what
helper program to call in order to handle a particular type of non-text
mail.  Note that metamail can also add multimedia support to certain
non-mail programs.

Metamail should be installed if you need to add multimedia support to
mail programs and some other programs, using the mailcap file.

%prep
%setup -q -n mm2.7
%patch0 -p1 -b .make
%patch1 -p1 -b .font
%patch2 -p1 -b .glibc
%patch3 -p1 -b .csh
%patch4 -p1 -b .tmpfiles
%patch5 -p1 -b .quote
%patch7 -p1 -b .sigh
%patch8 -p1 -b .arghhh
%patch9 -p1 -b .sml
%patch10 -p1
%patch11 -p1 -b .linux
%patch12 -p0 -b .manyvulns
%patch13 -p1 -b .gcc34
%patch14 -p1 -b .cve-2006-0709
%patch15 -p1 -b .gcc4

%build
cd src
%make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" basics

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{usr/bin,usr/lib/metamail/fonts,usr/man/man1}
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/metamail/fonts,%{_mandir}/man1}
cd src
make INSTROOT=$RPM_BUILD_ROOT%{_prefix} install-all INSTALL="install -c" MAN1DIR=$RPM_BUILD_ROOT/%{_mandir}/man1 MAN4DIR=$RPM_BUILD_ROOT/%{_mandir}/man4

install -m644 fonts/*.pcf $RPM_BUILD_ROOT%{_libdir}/metamail/fonts
install -m644 fonts/fonts.alias $RPM_BUILD_ROOT%{_libdir}/metamail/fonts
mkfontdir $RPM_BUILD_ROOT%{_libdir}/metamail/fonts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/metamail
%{_mandir}/man1/*
#%{_mandir}/man4/*

