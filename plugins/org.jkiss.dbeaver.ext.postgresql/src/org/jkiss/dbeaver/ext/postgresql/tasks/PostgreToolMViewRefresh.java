/*
 * DBeaver - Universal Database Manager
 * Copyright (C) 2010-2020 DBeaver Corp and others
 * Copyright (C) 2011-2012 Eugene Fradkin (eugene.fradkin@gmail.com)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.jkiss.dbeaver.ext.postgresql.tasks;

import org.jkiss.dbeaver.ext.postgresql.model.PostgreTableBase;
import org.jkiss.dbeaver.model.DBPEvaluationContext;
import org.jkiss.dbeaver.model.edit.DBEPersistAction;
import org.jkiss.dbeaver.model.exec.DBCException;
import org.jkiss.dbeaver.model.exec.DBCSession;
import org.jkiss.dbeaver.model.impl.edit.SQLDatabasePersistAction;
import org.jkiss.dbeaver.model.sql.task.SQLToolExecuteHandler;

import java.util.List;

public class PostgreToolMViewRefresh extends SQLToolExecuteHandler<PostgreTableBase, PostgreToolMViewRefreshSettings> {
    @Override
    public PostgreToolMViewRefreshSettings createToolSettings() {
        return new PostgreToolMViewRefreshSettings();
    }

    @Override
    public void generateObjectQueries(DBCSession session, PostgreToolMViewRefreshSettings settings, List<DBEPersistAction> queries, PostgreTableBase object) throws DBCException {
        String sql = "REFRESH MATERIALIZED VIEW " + object.getFullyQualifiedName(DBPEvaluationContext.DDL) + " ";
        boolean isWithData = settings.isWithData();
        if (isWithData) {
            sql += "WITH DATA";
        }
        else {
            sql += "WITH NO DATA";
        }
        queries.add(new SQLDatabasePersistAction(sql));
    }
}
