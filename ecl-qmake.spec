Name: ecl-qmake
Version: 0.1
Release: 1
Summary: ECL and EQL feature for qmake
Group: System/Base
License: GPLv2
Source0: %{name}-%{version}.tar.gz
URL: https://github.com/aardsoft/ecl-qmake
BuildRequires: libqt5-qtbase-common-devel

%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/mkspecs/features/*.prf


%prep
%setup -q


%build
qmake-qt5 ecl-qmake.pro


%install
make INSTALL_ROOT=%{buildroot} install
