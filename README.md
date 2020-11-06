# Reliably Github Action workflow demo
Repository demo for Reliably workflow with GitHub Action

This repository explains how to use Reliably as GitHub Action by providing
a simple [workflow](.github/workflows/reliably.yaml).

To run Reliably, simply use the action within your Github workflow YAML file:
```yaml
- name: Reliably
  uses: reliablyhq/gh-action@main
```

You can find more information on our action [repository](https://github.com/reliablyhq/gh-action).