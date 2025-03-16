# Bunna Bank Management System

## Overview
Bunna Bank Management System is an Odoo-based application designed to manage employees, branches, and loan requests efficiently. This system streamlines HR management, branch operations, and loan approvals within Bunna Bank.

## Features
- **Employee Management:** Add, edit, and manage employee details.
- **Branch Management:** Maintain branch records, including employees and loan-related data.
- **Loan Requests:** Handle loan applications with approval and tracking mechanisms.
- **User Permissions:** Secure access control using Odoo's role-based security model.

## Installation
### Prerequisites
Ensure you have the following installed:
- Ubuntu 22.04 or later
- Python 3.8+
- PostgreSQL
- Odoo 17

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/anuteshome/Bunna-Bank-Resl.git
   cd Bunna-Bank-Resl
   ```
2. **Move the Module to Odoo Addons Directory**
   ```bash
   sudo mv Bunna-Bank-Resl /opt/odoo/custom_addons/
   ```
3. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt  # If dependencies file exists
   ```
4. **Update Odoo Configuration**
   Edit your `odoo.conf` file to include the module path:
   ```ini
   addons_path = /opt/odoo/custom_addons
   ```
5. **Restart Odoo Server**
   ```bash
   sudo systemctl restart odoo
   ```
6. **Activate Developer Mode & Install the Module**
   - Go to Odoo UI → Apps → Activate Developer Mode.
   - Click **Update Apps List** and search for `Bunna Bank`.
   - Install the module.

## Usage
- Navigate to **Bunna Management** in the Odoo menu.
- Manage Employees, Branches, and Loan Requests easily through the provided views.
- Use role-based access to restrict operations.

## Security & Access Control
The system includes the following user access rules:
| Model              | Read | Write | Create | Delete |
|--------------------|------|-------|--------|--------|
| Employees         | ✅   | ✅    | ✅     | ✅     |
| Branches         | ✅   | ✅    | ✅     | ✅     |
| Loan Requests    | ✅   | ✅    | ✅     | ✅     |

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For inquiries or support, contact [your email] or raise an issue on the repository.

