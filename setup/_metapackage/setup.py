import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-akretion-odoo-viewer-groups",
    description="Meta package for akretion-odoo-viewer-groups Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-mrp_viewer',
        'odoo14-addon-project_viewer',
        'odoo14-addon-purchase_mrp_viewer',
        'odoo14-addon-purchase_report_viewer',
        'odoo14-addon-purchase_stock_viewer',
        'odoo14-addon-purchase_viewer',
        'odoo14-addon-sale_mrp_viewer',
        'odoo14-addon-sale_report_viewer',
        'odoo14-addon-sale_stock_viewer',
        'odoo14-addon-sale_viewer',
        'odoo14-addon-stock_report_viewer',
        'odoo14-addon-stock_viewer',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
