Summary:	CD player and ripper for GNOME
Summary(pl.UTF-8):   Odtwarzacz i ripper CD dla GNOME
Name:		goobox
Version:	0.9.93
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/goobox/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	d12dcf26907935ee4803107c572a5392
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-libnotify.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel >= 1:2.12.1
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.4.0
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gstreamer-devel >= 0.8.12
BuildRequires:	gstreamer-GConf-devel >= 0.8.12
BuildRequires:	gstreamer-plugins-devel >= 0.8.12
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	intltool
BuildRequires:	libbonobo-devel >= 2.8.1
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libnotify-devel >= 0.3.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	gnome-media-cddb >= 2.10.1
Requires:	gstreamer-cdparanoia >= 0.8.12
Requires:	libnotify >= 0.3.2
Requires:	notification-daemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CD player and ripper for GNOME.

%description -l pl.UTF-8
Odtwarzacz i ripper CD dla GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
gnome-doc-prepare --copy --force
%{__gnome_doc_common}
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

rm -rf $RPM_BUILD_ROOT%{_datadir}/{mime-info,application-registry}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install goobox.schemas
%scrollkeeper_update_post
%banner %{name} -e << EOF
To be able to rip a CD, You need to install appropriate
GStreamer plugins:
- gstreamer-audio-formats (encoding to WAVE)
- gstreamer-flac (encoding to FLAC)
- gstreamer-lame (encoding to MP3)
- gstreamer-vorbis (encoding to Ogg Vorbis)
EOF

%preun
%gconf_schema_uninstall goobox.schemas

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/goobox.schemas
%{_libdir}/bonobo/servers/*
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
