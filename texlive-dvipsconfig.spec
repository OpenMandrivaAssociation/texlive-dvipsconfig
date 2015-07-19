# revision 13293
# category Package
# catalog-ctan /dviware/dvipsconfig
# catalog-date 2007-03-05 22:02:45 +0100
# catalog-license gpl
# catalog-version 1.6
Name:		texlive-dvipsconfig
Version:	1.6
Release:	10
Summary:	Collection of dvips PostScript headers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvipsconfig
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipsconfig.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a collection of dvips PostScript header and dvips
config files. They control certain features of the printer,
including: A4, A3, usletter, simplex, duplex / long edge,
duplex / short edge, screen frequencies of images, black/white
invers, select transparency / paper for tektronix 550/560,
manual feeder, envelope feeder, and tray 1, 2 and 3, and
printing a PostScript grid underneath the page material--very
useful for measuring and eliminating paper feed errors!.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/dvipsconfig/README
%{_texmfdistdir}/dvips/dvipsconfig/addpsctrl
%{_texmfdistdir}/dvips/dvipsconfig/config.a3
%{_texmfdistdir}/dvips/dvipsconfig/config.a4
%{_texmfdistdir}/dvips/dvipsconfig/config.a4grid
%{_texmfdistdir}/dvips/dvipsconfig/config.duplong
%{_texmfdistdir}/dvips/dvipsconfig/config.dupshort
%{_texmfdistdir}/dvips/dvipsconfig/config.envelope
%{_texmfdistdir}/dvips/dvipsconfig/config.inv
%{_texmfdistdir}/dvips/dvipsconfig/config.manualfeed
%{_texmfdistdir}/dvips/dvipsconfig/config.mmgrid
%{_texmfdistdir}/dvips/dvipsconfig/config.psgrid
%{_texmfdistdir}/dvips/dvipsconfig/config.screen100
%{_texmfdistdir}/dvips/dvipsconfig/config.screen100_0
%{_texmfdistdir}/dvips/dvipsconfig/config.screen110
%{_texmfdistdir}/dvips/dvipsconfig/config.screen120
%{_texmfdistdir}/dvips/dvipsconfig/config.screen130
%{_texmfdistdir}/dvips/dvipsconfig/config.screen140
%{_texmfdistdir}/dvips/dvipsconfig/config.screen150
%{_texmfdistdir}/dvips/dvipsconfig/config.screen35
%{_texmfdistdir}/dvips/dvipsconfig/config.screen50
%{_texmfdistdir}/dvips/dvipsconfig/config.screen70
%{_texmfdistdir}/dvips/dvipsconfig/config.screen80
%{_texmfdistdir}/dvips/dvipsconfig/config.screen85
%{_texmfdistdir}/dvips/dvipsconfig/config.screen90
%{_texmfdistdir}/dvips/dvipsconfig/config.simplex
%{_texmfdistdir}/dvips/dvipsconfig/config.tek550paper
%{_texmfdistdir}/dvips/dvipsconfig/config.tek550transparency
%{_texmfdistdir}/dvips/dvipsconfig/config.tray1
%{_texmfdistdir}/dvips/dvipsconfig/config.tray2
%{_texmfdistdir}/dvips/dvipsconfig/config.tray3
%{_texmfdistdir}/dvips/dvipsconfig/config.usledger
%{_texmfdistdir}/dvips/dvipsconfig/config.usletter

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 751244
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 718287
- texlive-dvipsconfig
- texlive-dvipsconfig
- texlive-dvipsconfig
- texlive-dvipsconfig

