Summary:	KDE Interface for doing Mathematics and Scientific Computing
Name:		cantor
Version:	14.12.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/cantor/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	analitza-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libR)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:	pkgconfig(python)

%description
Cantor is a KDE Application aimed to provide a nice Interface
for doing Mathematics and Scientific Computing. It doesn't implement
its own Computation Logic, but instead is built around different
Backends.

%files
%doc README TODO
%doc %{_kde_docdir}/HTML/en/cantor
%{_kde_bindir}/cantor
%{_kde_bindir}/cantor_rserver
%{_kde_libdir}/kde4/cantor_advancedplotassistant.so
%{_kde_libdir}/kde4/cantor_creatematrixassistant.so
%{_kde_libdir}/kde4/cantor_differentiateassistant.so
%{_kde_libdir}/kde4/cantor_eigenvaluesassistant.so
%{_kde_libdir}/kde4/cantor_eigenvectorsassistant.so
%{_kde_libdir}/kde4/cantor_helppanelplugin.so
%{_kde_libdir}/kde4/cantor_importpackageassistant.so
%{_kde_libdir}/kde4/cantor_integrateassistant.so
%{_kde_libdir}/kde4/cantor_invertmatrixassistant.so
%{_kde_libdir}/kde4/cantor_luabackend.so
%{_kde_libdir}/kde4/cantor_maximabackend.so
%{_kde_libdir}/kde4/cantor_nullbackend.so
%{_kde_libdir}/kde4/cantor_octavebackend.so
%{_kde_libdir}/kde4/cantor_python2backend.so
%{_kde_libdir}/kde4/cantor_plot2dassistant.so
%{_kde_libdir}/kde4/cantor_plot3dassistant.so
%{_kde_libdir}/kde4/cantor_qalculatebackend.so
%{_kde_libdir}/kde4/cantor_qalculateplotassistant.so
%{_kde_libdir}/kde4/cantor_rbackend.so
%{_kde_libdir}/kde4/cantor_runscriptassistant.so
%{_kde_libdir}/kde4/cantor_sagebackend.so
%{_kde_libdir}/kde4/cantor_scilabbackend.so
%{_kde_libdir}/kde4/cantor_solveassistant.so
%{_kde_libdir}/kde4/cantor_variablemanagerplugin.so
%{_kde_libdir}/kde4/libcantorpart.so
%{_kde_libdir}/libcantor_config.so
%{_kde_applicationsdir}/cantor.desktop
%{_kde_appsdir}/cantor
%{_kde_iconsdir}/*/*/apps/cantor.*
%{_kde_iconsdir}/*/*/apps/luabackend.png
%{_kde_iconsdir}/*/*/apps/maximabackend.png
%{_kde_iconsdir}/*/*/apps/octavebackend.png
%{_kde_iconsdir}/*/*/apps/pythonbackend.png
%{_kde_iconsdir}/*/*/apps/qalculatebackend.png
%{_kde_iconsdir}/*/*/apps/rbackend.png
%{_kde_iconsdir}/*/*/apps/sagebackend.png
%{_kde_iconsdir}/*/*/apps/scilabbackend.png
%{_kde_configdir}/cantor*.knsrc
%{_kde_datadir}/appdata/cantor.appdata.xml
%{_kde_datadir}/config.kcfg/cantor.kcfg
%{_kde_datadir}/config.kcfg/cantor_libs.kcfg
%{_kde_datadir}/config.kcfg/luabackend.kcfg
%{_kde_datadir}/config.kcfg/maximabackend.kcfg
%{_kde_datadir}/config.kcfg/octavebackend.kcfg
%{_kde_datadir}/config.kcfg/python2backend.kcfg
%{_kde_datadir}/config.kcfg/qalculatebackend.kcfg
%{_kde_datadir}/config.kcfg/rserver.kcfg
%{_kde_datadir}/config.kcfg/sagebackend.kcfg
%{_kde_datadir}/config.kcfg/scilabbackend.kcfg
%{_kde_services}/cantor
%{_kde_servicetypes}/cantor_assistant.desktop
%{_kde_servicetypes}/cantor_backend.desktop
%{_kde_servicetypes}/cantor_panelplugin.desktop

#---------------------------------------------

%define cantorlibs_major 1
%define libcantorlibs %mklibname cantorlibs %{cantorlibs_major}

%package -n %{libcantorlibs}
Summary:	Runtime library for cantor
Group:		System/Libraries
Obsoletes:	%{mklibname cantorlibs 0} < %{EVRD}

%description -n %{libcantorlibs}
Runtime library for cantor.

%files -n %{libcantorlibs}
%{_kde_libdir}/libcantorlibs.so.0*
%{_kde_libdir}/libcantorlibs.so.%{cantorlibs_major}

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libcantorlibs} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde_libdir}/libcantorlibs.so
%{_includedir}/%{name}

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.1-1
- New version 4.14.1
- Update files

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.13.2-1
- New version 4.13.2
- Drop cantor-rpath patch (fixed upstream)

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.1-1
- New version 4.12.1
- Update files and BuildRequires (python)

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Thu Jul 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Mon Jul 02 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95
- libcantorlibs major should be 1, not 0

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.1-1
- update to 4.8.1

* Sun Feb 26 2012 Andrey Bondrov <abondrov@mandriva.org> 4.8.0-2
+ Revision: 780807
- Add BR pkgconfig(libqalculate) and analitza-devel, update file list

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762442
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758033
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744509
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 744238
- Fix file list
- Fix BR
- New upstream tarball
- New upstream tarball 4.7.80

* Mon Nov 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.41-1
+ Revision: 730560
- Import cantor

