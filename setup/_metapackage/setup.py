import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-akretion-odoo-viewer-groups",
    description="Meta package for akretion-odoo-viewer-groups Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-crm_viewer>=16.0dev,<16.1dev',
        'odoo-addon-mrp_viewer>=16.0dev,<16.1dev',
        'odoo-addon-project_viewer>=16.0dev,<16.1dev',
        'odoo-addon-purchase_mrp_viewer>=16.0dev,<16.1dev',
        'odoo-addon-purchase_report_viewer>=16.0dev,<16.1dev',
        'odoo-addon-purchase_stock_viewer>=16.0dev,<16.1dev',
        'odoo-addon-purchase_viewer>=16.0dev,<16.1dev',
        'odoo-addon-sale_mrp_viewer>=16.0dev,<16.1dev',
        'odoo-addon-sale_report_viewer>=16.0dev,<16.1dev',
        'odoo-addon-sale_stock_viewer>=16.0dev,<16.1dev',
        'odoo-addon-sale_viewer>=16.0dev,<16.1dev',
        'odoo-addon-stock_report_viewer>=16.0dev,<16.1dev',
        'odoo-addon-stock_viewer>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
