Summary:	QuickJS - A mighty JavaScript engine
Name:		quickjs-ng
Version:	0.10.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/quickjs-ng/quickjs/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	22b84e47c5c55fad7e8cbc9b5dad6944
URL:		https://quickjs-ng.github.io/quickjs/
BuildRequires:	cmake >= 3.16
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QuickJS is a small and embeddable JavaScript engine. It aims to
support the latest ECMAScript specification.

This project is a fork of the original QuickJS project by Fabrice
Bellard and Charlie Gordon, after it went dormant, with the intent of
reigniting its development.

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{name}.

%package progs
Summary:	Programs for %{name}
Summary(pl.UTF-8):	Programy dla programistów używających %{name}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description progs
qjs and qjsc programs.

%description progs -l pl.UTF-8
Programy qjs and qjsc.

%prep
%setup -q -n quickjs-%{version}

%build
%cmake -B build \
	-G Ninja

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost %{_libdir}/libqjs.so.0
%{_libdir}/libqjs.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/quickjs.h
%{_libdir}/cmake/quickjs
%{_libdir}/libqjs.so

%files progs
%defattr(644,root,root,755)
%doc examples
%attr(755,root,root) %{_bindir}/qjs
%attr(755,root,root) %{_bindir}/qjsc
