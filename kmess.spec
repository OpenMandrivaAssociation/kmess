%define name	 kmess
%define version	 2.0.0
%define release	 %mkrel 0.svn%{svn}.1
%define svn      4516

Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Graphical desktop/KDE
License:	GPLv2+
Source0:        http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.svn%{svn}.tar.bz2
Patch0:		kmess-2.0.0-linkage.patch
URL:		http://kmess.sourceforge.net
BuildRequires:	kdelibs4-devel
BuildRequires:  kdebase4-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	qca2 qca2-openssl qca2-devel
BuildRequires:	libxscrnsaver-devel
Requires:	qca2-openssl
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
Summary:	Yet another MSN messenger for KDE

%description
KMess is an easy-to-use MSN Messenger client for KDE. Install it
if you want an MSN Messenger client.

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS INSTALL TODO README ChangeLog
%{_kde_bindir}/%{name}
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*.desktop
%{_kde_datadir}/apps/%{name}
%{_kde_configdir}/*.knsrc
%{_kde_datadir}/applications/kde4/kmess.desktop
%{_kde_iconsdir}/*/*/apps/%{name}.*
%dir %{_kde_datadir}/emoticons/KMess-new
%{_kde_datadir}/emoticons/KMess-new/*.png
%{_kde_datadir}/emoticons/KMess-new/emoticons.xml
%{_kde_datadir}/sounds/%{name}*.ogg

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang %name --with-html

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT
