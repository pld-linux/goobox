Summary:	CD player and ripper for GNOME
Summary(pl.UTF-8):	Odtwarzacz i ripper CD dla GNOME
Name:		goobox
Version:	3.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goobox/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	4597122bd8f0b3acc5ee0e31e0e14b5a
Patch0:		%{name}-desktop.patch
URL:		https://people.gnome.org/~paobac/goobox/
BuildRequires:	brasero-devel >= 3
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libcoverart-devel >= 1.0.0
BuildRequires:	libdiscid-devel
BuildRequires:	libmusicbrainz5-devel >= 5.0.0
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	meson >= 0.43
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.40
Requires(post,postun):	gtk-update-icon-cache
Requires:	dbus(org.freedesktop.Notifications)
Requires:	glib2 >= 1:2.40
Requires:	gstreamer-cdparanoia >= 1.0.0
Requires:	gtk+3 >= 3.22.0
Requires:	hicolor-icon-theme
Requires:	libcoverart >= 1.0.0
Requires:	libnotify >= 0.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CD player and ripper for GNOME.

%description -l pl.UTF-8
Odtwarzacz i ripper CD dla GNOME.

%prep
%setup -q
%patch0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor
%banner %{name} -e << EOF
To be able to rip a CD, You need to install appropriate
GStreamer plugins:
- gstreamer-audio-formats (encoding to WAVE)
- gstreamer-flac (encoding to FLAC)
- gstreamer-lame (encoding to MP3)
- gstreamer-vorbis (encoding to Ogg Vorbis)
EOF

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/goobox
%{_datadir}/glib-2.0/schemas/org.gnome.Goobox.gschema.xml
%{_datadir}/metainfo/org.gnome.Goobox.appdata.xml
%{_desktopdir}/org.gnome.Goobox.desktop
%{_iconsdir}/hicolor/*x*/apps/goobox.png
%{_iconsdir}/hicolor/scalable/apps/goobox-symbolic.svg
