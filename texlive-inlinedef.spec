# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/inlinedef
# catalog-date 2008-08-19 23:32:24 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-inlinedef
Version:	1.0
Release:	4
Summary:	Inline expansions within definitions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/inlinedef
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinedef.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinedef.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinedef.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a macro \Inline. that precedes a \def or
\gdef. Within the definition text of an inlined definition,
keywords such as \Expand may be used to selectively inline
certain expansions at definition-time. This eases the process
of redefining macros in terms of the original definition, as
well as definitions in which the token that must be expanded is
deep within, where \expandafter would be difficult and \edef is
not suitable. Another application is as an easier version of
\aftergroup, by defining a macro in terms of expanded local
variables, then ending the group with
\expandafter\endgroup\macro.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/inlinedef/inlinedef.sty
%doc %{_texmfdistdir}/doc/latex/inlinedef/README
%doc %{_texmfdistdir}/doc/latex/inlinedef/inlinedef.pdf
%doc %{_texmfdistdir}/doc/latex/inlinedef/inlinetest.tex
#- source
%doc %{_texmfdistdir}/source/latex/inlinedef/inlinedef.dtx
%doc %{_texmfdistdir}/source/latex/inlinedef/inlinedef.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752794
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718720
- texlive-inlinedef
- texlive-inlinedef
- texlive-inlinedef
- texlive-inlinedef

