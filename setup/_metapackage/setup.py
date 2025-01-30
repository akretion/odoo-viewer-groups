import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-akretion-odoo-viewer-groups",
    description="Meta package for akretion-odoo-viewer-groups Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_report_viewer',
        'odoo12-addon-account_viewer',
        'odoo12-addon-account_voucher_viewer',
        'odoo12-addon-mrp_viewer',
        'odoo12-addon-project_viewer',
        'odoo12-addon-purchase_report_viewer',
        'odoo12-addon-purchase_stock_viewer',
        'odoo12-addon-purchase_viewer',
        'odoo12-addon-sale_report_viewer',
        'odoo12-addon-sale_stock_viewer',
        'odoo12-addon-sale_viewer',
        'odoo12-addon-stock_report_viewer',
        'odoo12-addon-stock_viewer',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
