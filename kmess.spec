%define name	 kmess
%define version	 1.5
%define release	 %mkrel 0.pre1.1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Graphical desktop/KDE
License:	GPL
Source0:        http://ovh.dl.sourceforge.net/sourceforge/kmess/%{name}-%{version}pre1.tar.bz2

URL:		http://kmess.sourceforge.net
BuildRequires:  kdebase-devel
BuildRequires:	kdenetwork-devel
BuildRequires:  libxslt-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
Summary:	Yet another MSN messenger for KDE


%description
KMess is an easy-to-use MSN Messenger client for KDE. Install it
if you want an MSN Messenger client.

%prep
%setup -q -n %{name}-%{version}pre1


%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure	--build=%{_target_platform} \
		--prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--disable-debug \
		--enable-mt \
		--enable-shared \
		--disable-static \
		--disable-objprelink \
		--with-pic \
		--with-gnu-ld \
		--disable-rpath \
		--disable-embedded \
		--enable-fast-install=yes \
		--with-qt-dir=%{_prefix}/lib/qt3 \
		--with-xinerama 
#		--enable-final
#		do not use this, makes kmess fail to compile

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

install -d $RPM_BUILD_ROOT/%{_menudir}
kdedesktop2mdkmenu.pl %{name} "Networking/Instant messaging" $RPM_BUILD_ROOT%{_datadir}/applications/kde/kmess.desktop $RPM_BUILD_ROOT%{_menudir}/%{name} kde
install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

#Relativisation of symlink, rpm fails to do it
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/%{name}/common
ln -sf ../common $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/%{name}/common

%find_lang %{name}

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc %{_docdir}/HTML/*/%{name}
%doc AUTHORS INSTALL TODO README ChangeLog
%{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/applications/kde/kmess.desktop
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/22x22/apps/kmess.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/64x64/apps/kmess.png
%{_iconsdir}/hicolor/128x128/apps/kmess.png
%{_iconsdir}/locolor/16x16/apps/%{name}.png
%{_iconsdir}/locolor/22x22/apps/kmess.png
%{_iconsdir}/locolor/32x32/apps/%{name}.png
%dir %{_datadir}/emoticons/KMess-new
%{_datadir}/emoticons/KMess-new/*.png
%{_datadir}/emoticons/KMess-new/emoticons.xml
%{_datadir}/sounds/%{name}*.ogg
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_menudir}/%{name}



