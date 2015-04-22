Name     : rubygem-thor
Version  : 0.19.1
Release  : 5
URL      : https://rubygems.org/downloads/thor-0.19.1.gem
Source0  : https://rubygems.org/downloads/thor-0.19.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-thor-bin
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-docile
BuildRequires : rubygem-domain_name
BuildRequires : rubygem-fakeweb
BuildRequires : rubygem-http-cookie
BuildRequires : rubygem-mime-types
BuildRequires : rubygem-netrc
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rest-client
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-html
BuildRequires : rubygem-term-ansicolor
BuildRequires : rubygem-thor
BuildRequires : rubygem-tins
BuildRequires : rubygem-unf
BuildRequires : rubygem-unf_ext

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
/usr/lib64/ruby/gems/2.2.0/cache/thor-0.19.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/IO/cdesc-IO.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Object/namespace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Object/rake_namespace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Object/task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/ClassMethods/add_runtime_options%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/ClassMethods/source_paths-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/ClassMethods/source_paths_for_search-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/ClassMethods/source_root-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/CreateFile/cdesc-CreateFile.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/CreateLink/cdesc-CreateLink.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/Directory/cdesc-Directory.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/EmptyDirectory/cdesc-EmptyDirectory.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/InjectIntoFile/cdesc-InjectIntoFile.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/add_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/add_link-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/append_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/append_to_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/apply-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/behavior-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/capture-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/cdesc-Actions.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/chmod-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/comment_lines-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/concat-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/copy_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/create_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/create_link-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/destination_root%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/destination_root-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/directory-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/empty_directory-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/find_in_source_paths-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/gsub_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/in_root-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/inject_into_class-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/inject_into_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/insert_into_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/inside-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/link_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/output_buffer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/prepend_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/prepend_to_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/relative_to_original_destination_root-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/remove_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/remove_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/run_ruby_script-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/source_paths-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/template-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/thor-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Actions/uncomment_lines-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/AmbiguousCommandError/cdesc-AmbiguousCommandError.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Argument/cdesc-Argument.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Arguments/cdesc-Arguments.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/all_commands-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/all_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/argument-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/arguments-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/basename-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/check_unknown_options%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/class_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/class_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/commands-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/exit_on_failure%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/from_superclass-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/group-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/inherited-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/method_added-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/namespace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/no_commands-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/no_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/print_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/public_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/public_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/remove_argument-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/remove_class_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/remove_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/remove_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/strict_args_position%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/ClassMethods/tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/args-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/cdesc-Base.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/parent_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/shell-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/subclass_files-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Base/subclasses-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/cdesc-Command.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/formatted_usage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/handle_argument_error%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/handle_no_method_error%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/hidden%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/local_method%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/not_debugging%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/private_method%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/required_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Command/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/CoreExt/HashWithIndifferentAccess/cdesc-HashWithIndifferentAccess.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/CoreExt/OrderedHash/cdesc-OrderedHash.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/CoreExt/cdesc-CoreExt.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/DynamicCommand/cdesc-DynamicCommand.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/DynamicCommand/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/DynamicCommand/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Error/cdesc-Error.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Group/banner-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Group/cdesc-Group.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Group/desc-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Group/help-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Group/invoke-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Group/invoke_from_option-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Group/printable_commands-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Group/printable_tasks-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Group/remove_invocation-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/HiddenCommand/cdesc-HiddenCommand.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/HiddenCommand/hidden%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Invocation/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Invocation/cdesc-Invocation.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Invocation/current_command_chain-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Invocation/invoke-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Invocation/invoke_with_padding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/InvocationError/cdesc-InvocationError.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Basic/available%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Basic/cdesc-Basic.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Basic/echo%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Basic/get_input-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Basic/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Basic/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Basic/prompt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Basic/readline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/PathCompletion/absolute_matches-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/PathCompletion/base_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/PathCompletion/cdesc-PathCompletion.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/PathCompletion/glob_pattern-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/PathCompletion/matches-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/PathCompletion/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/PathCompletion/relative_matches-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/PathCompletion/text-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/add_to_history%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/available%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/cdesc-Readline.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/completion_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/completion_proc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/readline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/Readline/use_path_completion%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/best_available-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/cdesc-LineEditor.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/LineEditor/readline-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/MalformattedArgumentError/cdesc-MalformattedArgumentError.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Option/cdesc-Option.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Options/cdesc-Options.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/RakeCompat/Rake/cdesc-Rake.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/RakeCompat/cdesc-RakeCompat.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/RakeCompat/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/RakeCompat/rake_classes-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/RequiredArgumentMissingError/cdesc-RequiredArgumentMissingError.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Runner/cdesc-Runner.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Sandbox/cdesc-Sandbox.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/as_unicode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/ask-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/ask_filtered-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/ask_simply-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/base-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/can_display_colors%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/cdesc-Basic.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/dynamic_width-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/dynamic_width_stty-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/dynamic_width_tput-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/file_collision-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/lookup_color-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/mute%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/mute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/no%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/padding%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/padding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/prepare_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/print_in_columns-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/print_table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/print_wrapped-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/say-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/say_status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/stderr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/stdout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/terminal_width-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/truncate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/unix%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Basic/yes%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Color/can_display_colors%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Color/cdesc-Color.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/Color/set_color-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/HTML/ask-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/HTML/can_display_colors%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/HTML/cdesc-HTML.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/HTML/set_color-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/cdesc-Shell.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/shell-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Shell/with_padding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/UndefinedCommandError/cdesc-UndefinedCommandError.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/UnknownArgumentError/cdesc-UnknownArgumentError.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/camel_case-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/cdesc-Util.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/escape_globs-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/find_by_namespace-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/find_class_and_command_by_namespace-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/find_class_and_task_by_namespace-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/globs_for-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/load_thorfile-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/namespace_from_thor_class-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/namespaces_in_content-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/ruby_command-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/snake_case-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/thor_classes_in-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/thor_root-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/thor_root_glob-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/Util/user_home-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/banner-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/cdesc-Thor.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/check_unknown_options%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/command_help-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/default_command-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/default_task-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/desc-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/find_command_possibilities-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/find_task_possibilities-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/help-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/help-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/long_desc-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/map-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/method_option-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/method_options-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/option-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/options-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/package_name-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/printable_commands-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/printable_tasks-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/register-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/stop_on_unknown_option%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/subcommand-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/subcommand_classes-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/subcommand_help-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/subcommands-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/subtask-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/subtask_help-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/subtasks-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/Thor/task_help-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thor-0.19.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/.document
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/LICENSE.md
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/README.md
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/Thorfile
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/bin/thor
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/coverage/*
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/coverage/.last_run.json
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/coverage/.resultset.json
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/coverage/.resultset.json.lock
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/actions.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/actions/create_file.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/actions/create_link.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/actions/directory.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/actions/empty_directory.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/actions/file_manipulation.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/actions/inject_into_file.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/base.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/command.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/core_ext/hash_with_indifferent_access.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/core_ext/io_binary_read.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/core_ext/ordered_hash.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/error.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/group.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/invocation.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/line_editor.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/line_editor/basic.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/line_editor/readline.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/parser.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/parser/argument.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/parser/arguments.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/parser/option.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/parser/options.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/rake_compat.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/runner.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/shell.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/shell/basic.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/shell/color.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/shell/html.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/util.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/lib/thor/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/actions/create_file_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/actions/create_link_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/actions/directory_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/actions/empty_directory_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/actions/file_manipulation_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/actions/inject_into_file_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/actions_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/base_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/command_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/core_ext/hash_with_indifferent_access_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/core_ext/ordered_hash_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/exit_condition_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/fixtures/*
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/group_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/invocation_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/line_editor/basic_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/line_editor/readline_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/line_editor_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/parser/argument_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/parser/arguments_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/parser/option_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/parser/options_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/quality_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/rake_compat_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/register_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/runner_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/sandbox/
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/shell/basic_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/shell/color_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/shell/html_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/shell_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/subcommand_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/thor_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/spec/util_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/thor-0.19.1/thor.gemspec
/usr/lib64/ruby/gems/2.2.0/specifications/thor-0.19.1.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/thor
