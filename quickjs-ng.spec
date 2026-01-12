#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	QuickJS - A mighty JavaScript engine
Name:		quickjs-ng
Version:	0.11.0
Release:	2
License:	MIT
Group:		Libraries
Source0:	https://github.com/quickjs-ng/quickjs/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	3807493185e8aa5265e67d954b6f18e0
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

%description -l pl.UTF-8
QuickJS jest małym i osadzalnym silnikiem JavaScriptu. Stara się
był zgodnym z najnowszą specyfikacją ECMAScriptu.

Ten projekt jest forkiem oryginalnego QuickJS napisanego przez
Fabrice'a Bellarda i Charlie Gordona, po tym jak był zastój
w rozwoju QuickJS-a, z myślą przyspieszenia jego rozwoju.

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

%package static
Summary:	Static quickjs-ng library
Summary(pl.UTF-8):	Statyczna biblioteka quickjs-ng
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static quickjs-ng library.

%description static -l pl.UTF-8
Statyczna biblioteka quickjs-ng.

%prep
%setup -q -n quickjs-%{version}

%build
%if %{with static_libs}
%cmake -B build-static \
	-G Ninja \
	-DBUILD_SHARED_LIBS=OFF
%ninja_build -C build-static
%endif

%cmake -B build \
	-G Ninja

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%ninja_install -C build-static
%endif

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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libqjs.a
%endif
