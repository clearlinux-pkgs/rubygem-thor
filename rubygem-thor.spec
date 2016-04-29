Name     : rubygem-thor
Version  : 0.19.1
Release  : 9
URL      : https://rubygems.org/downloads/thor-0.19.1.gem
Source0  : https://rubygems.org/downloads/thor-0.19.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-thor-bin
BuildRequires : ruby
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-docile
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-html

%description
__start__
__end__

%package bin
Summary: bin components for the rubygem-thor package.
Group: Binaries

%description bin
bin components for the rubygem-thor package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n thor-0.19.1
gem spec %{SOURCE0} -l --ruby > rubygem-thor.gemspec

%build
gem build rubygem-thor.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
thor-0.19.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/thor-0.19.1
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/thor-0.19.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/.document
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/LICENSE.md
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/Thorfile
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/bin/thor
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/actions.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/actions/create_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/actions/create_link.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/actions/directory.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/actions/empty_directory.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/actions/file_manipulation.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/actions/inject_into_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/command.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/core_ext/hash_with_indifferent_access.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/core_ext/io_binary_read.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/core_ext/ordered_hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/group.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/invocation.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/line_editor.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/line_editor/basic.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/line_editor/readline.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/parser/argument.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/parser/arguments.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/parser/option.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/parser/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/rake_compat.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/shell.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/shell/basic.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/shell/color.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/shell/html.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/util.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/lib/thor/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/actions/create_file_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/actions/create_link_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/actions/directory_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/actions/empty_directory_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/actions/file_manipulation_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/actions/inject_into_file_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/actions_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/base_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/command_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/core_ext/hash_with_indifferent_access_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/core_ext/ordered_hash_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/exit_condition_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/application.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/app{1}/README
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/bundle/execute.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/bundle/main.thor
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/command.thor
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/doc/%file_name%.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/doc/COMMENTER
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/doc/README
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/doc/block_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/doc/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/doc/config.yaml.tt
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/doc/excluding/%file_name%.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/fixtures/*
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/group_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/invocation_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/line_editor/basic_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/line_editor/readline_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/line_editor_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/parser/argument_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/parser/arguments_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/parser/option_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/parser/options_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/quality_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/rake_compat_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/register_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/runner_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/application.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/app{1}/README
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/bundle/execute.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/bundle/main.thor
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/command.thor
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/doc/%file_name%.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/doc/COMMENTER
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/doc/README
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/doc/block_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/doc/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/doc/config.yaml.tt
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/doc/excluding/%file_name%.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/sandbox/*
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/shell/basic_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/shell/color_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/shell/html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/shell_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/subcommand_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/thor_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/spec/util_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/thor-0.19.1/thor.gemspec
/usr/lib64/ruby/gems/2.3.0/specifications/thor-0.19.1.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/thor
