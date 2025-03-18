# demo-pipeline
Demo a full pipeline: code to cloud with Scribe instrumentation and uploading of evidence

To try it out:
1. Scribe will set up a fork of this repo with appropreiate secrets set.
2. Scribe shall walk you through running the workflows and understanding the results.


The code includes:
- A `package.json` file with a `start` script that imports a KEV vulnerable module [CVE-2021-21315](https://nvd.nist.gov/vuln/detail/CVE-2021-21315) 
- A python script with a secret in the code

