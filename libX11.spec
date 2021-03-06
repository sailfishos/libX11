# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       libX11

# >> macros
# << macros

Summary:    X.Org X11 libX11 runtime library
Version:    1.5.0
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
Source100:  libX11.yaml
Requires:   xorg-x11-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xcb) >= 1.1.92
BuildRequires:  pkgconfig(xf86bigfontproto) >= 1.2.0
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  fdupes

%description
The X.org libX11 runtime library

%package devel
Summary:    X.Org X11 libX11 development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The libX11 development package


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --disable-dependency-tracking \
    --enable-specs=no

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%fdupes  %{buildroot}//usr/share/man/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING README NEWS
%dir %{_datadir}/X11
%{_datadir}/X11/locale/
%{_datadir}/X11/XErrorDB
%{_libdir}/libX11.so.6
%{_libdir}/libX11.so.6.3.0
%{_libdir}/libX11-xcb.so.1
%{_libdir}/libX11-xcb.so.1.0.0
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%dir %{_includedir}/X11
%{_includedir}/X11/ImUtil.h
%{_includedir}/X11/XKBlib.h
%{_includedir}/X11/Xcms.h
%{_includedir}/X11/Xlib.h
%{_includedir}/X11/XlibConf.h
%{_includedir}/X11/Xlibint.h
%{_includedir}/X11/Xlib-xcb.h
%{_includedir}/X11/Xlocale.h
%{_includedir}/X11/Xregion.h
%{_includedir}/X11/Xresource.h
%{_includedir}/X11/Xutil.h
%{_includedir}/X11/cursorfont.h
%{_libdir}/libX11.so
%{_libdir}/libX11-xcb.so
%{_libdir}/X11/Xcms.txt
%{_libdir}/pkgconfig/x11.pc
%{_libdir}/pkgconfig/x11-xcb.pc
%doc %{_mandir}/man3/*.3*
%doc %{_mandir}/man5/*.5*
# << files devel
