%define		rel	0.1
%define		snap	20151116
Summary:	Utilities for aufs
Name:		aufs-util
Version:	4.0
Release:	0.%{snap}.%{rel}
License:	GPL v2
Group:		Base/Kernel
# git archive -v --prefix=${P}/ --remote=git://git.code.sf.net/p/aufs/aufs-util aufs4.0 -o ${P}.tar
# xz -ve9 *.tar
Source0:	https://dev.gentoo.org/~jlec/distfiles/%{name}-%{version}_p%{snap}.tar.xz
# Source0-md5:	a1e9a7e370f7fefd08abe70e1900c812
Patch0:		buildflags.patch
URL:		http://aufs.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities are always necessary for aufs

%prep
%setup -q -n %{name}-%{version}_p%{snap}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man5,%{_sbindir}}
cp -p util/{mount.aufs,umount.aufs,auplink,aulchown} $RPM_BUILD_ROOT%{_sbindir}
cp -p util/aufs.5 $RPM_BUILD_ROOT%{_mandir}/man5/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.aufs1 README.aufs2 History
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man5/*
