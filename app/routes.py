from flask import current_app, jsonify
from . import db
from .models import Tool

@current_app.route('/tools', methods=['GET'])
def get_tools():
    tools = Tool.query.all()
    return jsonify([tool.to_dict() for tool in tools])

@current_app.route('/tool/<int:tool_id>', methods=['GET'])
def get_tool(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    return jsonify(tool.to_dict())

@current_app.route('/metrics', methods=['GET'])
def get_metrics():
    total_tools = Tool.query.count()
    active_tools = Tool.query.filter_by(status='active').count()
    return jsonify({
        'total_tools': total_tools,
        'active_tools': active_tools,
        'utilization_rate': (active_tools / total_tools) * 100 if total_tools > 0 else 0
    })
