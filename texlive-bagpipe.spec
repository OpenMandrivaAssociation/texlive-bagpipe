%global tl_name bagpipe
%global tl_revision 34393

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.02
Release:	%{tl_revision}.1
Summary:	Support for typesetting bagpipe music
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/bagpipe
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bagpipe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bagpipe.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typesetting bagpipe music in MusixTeX is needlessly tedious. This
package provides specialized and re-defined macros to simplify this
task.

