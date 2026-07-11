%global tl_name inlinedef
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Inline expansions within definitions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/inlinedef
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinedef.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinedef.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinedef.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a macro \Inline that precedes a \def or \gdef.
Within the definition text of an inlined definition, keywords such as
\Expand may be used to selectively inline certain expansions at
definition-time. This eases the process of redefining macros in terms of
the original definition, as well as definitions in which the token that
must be expanded is deep within, where \expandafter would be difficult
and \edef is not suitable. Another application is as an easier version
of \aftergroup, by defining a macro in terms of expanded local
variables, then ending the group with \expandafter\endgroup\macro.

