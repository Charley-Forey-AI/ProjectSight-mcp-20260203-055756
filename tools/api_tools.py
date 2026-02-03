"""Generated API tools: register_tools(mcp) to attach all tools."""

def register_tools(mcp):
    from core import api_client

    @mcp.tool()
    def Account_GetAccounts() -> dict:
        """Get Accounts"""
        path_params = {}
        query_params = None
        result = api_client.call("/accounts", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Account_GetPortfoliosForAccount(accountId, includeDisabled=None, includeOffline=None) -> dict:
        """Get Portfolios for the specific account"""
        path_params = {"accountId": accountId}
        query_params = {"includeDisabled": includeDisabled, "includeOffline": includeOffline}
        result = api_client.call("/accounts/{accountId}/portfolios", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Company_List(portfolioGuid, offset=None, limit=None) -> dict:
        """Get Collection of Company records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/Companies", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Company_ListOnly(portfolioGuid, offset=None, limit=None) -> dict:
        """Get Collection of Company records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/Companies/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Company_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Company"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/Companies/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetCompaniesForAccount(accountId) -> dict:
        """Retrieves the list of ERP Companies for the specified account from the ERP cache"""
        path_params = {"accountId": accountId}
        query_params = None
        result = api_client.call("/accounts/{accountId}/erpCompanies", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetCustomersAndVendorsForAccount(accountId) -> dict:
        """Retrieves the list of ERP Customer and Vendors for the specified account from the ERP cache"""
        path_params = {"accountId": accountId}
        query_params = None
        result = api_client.call("/accounts/{accountId}/erpCustomersAndVendors", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ERPReadOnly_GetProjectsForAccount(accountId) -> dict:
        """Retrieves the list of ERP Projects for the specified account from the ERP cache"""
        path_params = {"accountId": accountId}
        query_params = None
        result = api_client.call("/accounts/{accountId}/erpProjects", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Portfolio_GetPortfolios(includeOffline=None) -> dict:
        """Get Portfolios"""
        path_params = {}
        query_params = {"includeOffline": includeOffline}
        result = api_client.call("/portfolios", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Portfolio_GetByID(portfolioGuid) -> dict:
        """Get Individual Portfolio"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/portfolios/{portfolioGuid}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_GetByID(portfolioGuid, projectId, rfiId) -> dict:
        """Get Individual RFI Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "rfiId": rfiId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis/{rfiId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of RFI records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of RFI records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/rfis/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of RFI records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of RFI records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/rfis/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get Workflow states for RFI records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for RFI records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/rfis/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for RFI"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/rfis/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def RFI_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for RFI"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/rfis/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Records_GetOpenAssignmentsForAllPortfolios() -> dict:
        """Get information on all open assignments for a user in all Portfolios the user has access to"""
        path_params = {}
        query_params = None
        result = api_client.call("/records/assignments", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Records_GetOpenAssignmentSummariesForAllPortfolios() -> dict:
        """Get summary information on all open assignments for a user in all Portfolios the user has access to. An additional call to /records/assignments/details is required to obtain the details per table type"""
        path_params = {}
        query_params = None
        result = api_client.call("/records/assignments/summaries", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result