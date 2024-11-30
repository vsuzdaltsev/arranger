# How to Add a New Terraform Provider

This example demonstrates how to add Terraform **"hashicorp/local"** provider.

### Steps:

1. Create an empty `tmp` directory within the Docker container and run the following command:
   ```shell
   $ cdktf init --providers "hashicorp/local" --providers-force-local --template python
   ```

   1. When prompted:
      - **Do you want to continue with Terraform Cloud remote state management? (Y/n)**  
        Select: `N`

   2. For the **Project Name**, press `Enter`.

   3. For the **Project Description**, press `Enter`.

   4. When prompted:
      - **Do you want to send crash reports to the CDKTF team? (Y/n)**  
        Select: `N`

   5. Wait for CDKTF to finish initialization.
2. Inside the `tmp` directory, copy the newly created `imports/local` directory to `python3/packages/arranger_cdktf/arranger_cdktf/imports`:
   ```shell
   cp -r imports/local ../python3/packages/sd_cdktf/sd_cdktf/imports
   ```
3. Add the provider name to `python3/packages/arranger_cdktf/arranger_cdktf/imports/__init__.py`
4. Return back to the root directory of the project and run:
   ```shell
   $ inv python3.build-and-install -p arranger_cdktf
   ```

5. Add to `python3/packages/arranger_globals/arranger_globals/cdktf_globals.py`

   ```python
   def local_provider(self, scope) -> Any:
        from arranger_cdktf.imports.local.provider import LocalProvider

        return LocalProvider(scope=scope, id="local-provider")
   ```

6. Run
   ```shell
   $ inv python3.build-and-install -p arranger_globals
   ```
7. Remove `tmp` dir
   