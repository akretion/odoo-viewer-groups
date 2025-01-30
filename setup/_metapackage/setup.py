import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-akretion-odoo-viewer-groups",
    description="Meta package for akretion-odoo-viewer-groups Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-account_report_viewer',
        'odoo10-addon-account_viewer',
        'odoo10-addon-account_voucher_viewer',
        'odoo10-addon-mrp_viewer',
        'odoo10-addon-project_viewer',
        'odoo10-addon-purchase_report_viewer',
        'odoo10-addon-purchase_viewer',
        'odoo10-addon-sale_mrp_viewer',
        'odoo10-addon-sale_report_viewer',
        'odoo10-addon-sale_stock_viewer',
        'odoo10-addon-sale_viewer',
        'odoo10-addon-stock_report_viewer',
        'odoo10-addon-stock_viewer',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 10.0',
    ]
)
