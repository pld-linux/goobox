# TODO:
#	- maybe some info that you need to install proper
#	  gstreamer plugins if you want to rip a CD
#
Summary:	CD player and ripper for GNOME
Summary(pl):	Odtwarzacz i ripper CD dla GNOME
Name:		goobox
Version:	0.7.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	aeecf6fa7dd58c1eb832c49c880c0c0c
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel >= 2.3.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-media-devel >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.6.0
BuildRequires:	gstreamer-GConf-devel >= 0.8.0
BuildRequires:	gstreamer-devel >= 0.8.0
BuildRequires:	gstreamer-plugins-devel >= 0.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
BuildRequires:	libbonobo-devel >= 2.6.0
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	gnome-media >= 2.8.0
Requires:	gstreamer-cdparanoia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CD player and ripper for GNOME.

%description -l pl
Odtwarzacz i ripper CD dla GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -f po/no.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome

%post
%gconf_schema_install
/usr/bin/scrollkeeper-update

%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/application-registry/*
%{_libdir}/bonobo/servers/*
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
