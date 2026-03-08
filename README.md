```markdown
# ansible_projects

Collection of automation projects and playbooks built with **Ansible** for system configuration, deployment, and infrastructure management.

## Overview

This repository contains various Ansible automation examples and projects that can be used to:

- Automate server configuration
- Deploy services and applications
- Manage infrastructure using Infrastructure as Code (IaC)
- Standardize environment setup

Ansible is an open-source automation platform used for configuration management, application deployment, and orchestration. It works agentless and communicates with remote systems mainly through SSH. 

## Repository Structure

Example structure of the repository:

```

ansible_projects/
│
├── inventory/
│   └── hosts
│
├── playbooks/
│   ├── site.yml
│   └── example_playbook.yml
│
├── roles/
│   ├── common/
│   ├── webserver/
│   └── database/
│
├── group_vars/
├── host_vars/
└── README.md

````

### Description

- **inventory/** – Inventory files that define managed hosts
- **playbooks/** – Ansible playbooks used to execute tasks
- **roles/** – Reusable roles for modular automation
- **group_vars/** – Variables applied to host groups
- **host_vars/** – Variables applied to specific hosts

## Requirements

Before using these playbooks you need:

- Python 3.x
- Ansible installed on the control machine
- SSH access to target hosts

Install Ansible with:

```bash
pip install ansible
````

or

```bash
sudo apt install ansible
```

## Usage

1. Clone the repository

```bash
git clone https://github.com/msabetta/ansible_projects.git
cd ansible_projects
```

2. Edit the inventory file

```
inventory/hosts
```

Example:

```
[all]
master1.local
master2.local
worker1.local
worker2.local
worker3.local
worker4.local
worker5.local

[master]
master1.local
master2.local

[workers]
worker1.local
worker2.local
worker3.local
worker4.local
worker5.local
```

3. Run a playbook

```bash
ansible-playbook -i inventory/hosts playbooks/create_user.yml
```

## Example Playbook Execution

```bash
ansible-playbook -i inventory/hosts playbooks/example_playbook.yml
```

## Best Practices

* Use **roles** to keep playbooks modular
* Store environment-specific variables in `group_vars`
* Keep secrets encrypted using **Ansible Vault**
* Test playbooks in staging before production

## Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a new branch
3. Submit a Pull Request

## License

This project is distributed under the MIT License unless otherwise specified.