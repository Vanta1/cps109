{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }: let
    name = "python default";
  in
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs {
          inherit system;
        };
      in
        with pkgs; {
          devShells.default = mkShell {
            packages = [
              pkgs.python313
              pkgs.python313Packages.python-lsp-server
            ];
            shellHook = ''
              echo "entering ${name} devshell"
            '';
          };
        }
    );
}
