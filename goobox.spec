# TODO:
#	- maybe some info that you need to install proper
#	  gstreamer plugins if you want to rip a CD
#
Summary:	CD player and ripper for GNOME
Summary(pl):	Odtwarzacz i ripper CD dla GNOME
Name:		goobox
Version:	0.6.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	1b3ef5e6c08059f179f428cfcfe7a8ae
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel >= 2.3.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libbonobo-devel >= 2.6.0
BuildRequires:	gnome-vfs2-devel >= 2.6.0
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	gnome-media-devel >= 2.8.0
BuildRequires:	gstreamer-devel >= 0.8.0
BuildRequires:	gstreamer-plugins-devel
BuildRequires:	gstreamer-GConf-devel
BuildRequires:	intltool
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

%build
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

%find_lang %{name}

%post
%gconf_schema_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/application-registry/*
%{_libdir}/bonobo/servers/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
