package org.jkiss.dbeaver.ext.postgresql.tasks;

import org.jkiss.dbeaver.ext.postgresql.model.PostgreTableBase;
import org.jkiss.dbeaver.model.DBPEvaluationContext;
import org.jkiss.dbeaver.model.edit.DBEPersistAction;
import org.jkiss.dbeaver.model.exec.DBCException;
import org.jkiss.dbeaver.model.exec.DBCSession;
import org.jkiss.dbeaver.model.impl.edit.SQLDatabasePersistAction;
import org.jkiss.dbeaver.model.sql.task.SQLToolExecuteHandler;

import java.util.List;

public class PostgreToolTableAnalyze extends SQLToolExecuteHandler<PostgreTableBase, PostgreToolTableAnalyzeSettings> {
    @Override
    public PostgreToolTableAnalyzeSettings createToolSettings() {
        return new PostgreToolTableAnalyzeSettings();
    }

    @Override
    public void generateObjectQueries(DBCSession session, PostgreToolTableAnalyzeSettings settings, List<DBEPersistAction> queries, PostgreTableBase object) throws DBCException {
        String sql = "ANALYZE VERBOSE " + object.getFullyQualifiedName(DBPEvaluationContext.DDL);
        queries.add(new SQLDatabasePersistAction(sql));
    }
}
