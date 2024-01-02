// server side
import io.socket.*;
import org.json.*;
public class Server {
  public static void main (String[] args) {
    try {
      // create a socket server
      SocketServer server = new SocketServer (80);
      // listen for connection events
      server.on ("connection", new Emitter.Listener () {
        @Override
        public void call (Object... args) {
          // get the connected socket
          Socket socket = (Socket) args [0];
          // join a room based on user id
          socket.on ("join", new Emitter.Listener () {
            @Override
            public void call (Object... args) {
              try {
                // get the user id from the data
                JSONObject data = (JSONObject) args [0];
                String userId = data.getString ("userId");
                // join the room with the user id
                socket.join (userId);
              } catch (JSONException e) {
                e.printStackTrace ();
              }
            }
          });
          // send a message to a specific user
          socket.on ("send", new Emitter.Listener () {
            @Override
            public void call (Object... args) {
              try {
                // get the message data from the data
                JSONObject data = (JSONObject) args [0];
                String to = data.getString ("to");
                String from = data.getString ("from");
                String message = data.getString ("message");
                // emit a receive event to the room with the recipient user id
                server.to (to).emit ("receive", new JSONObject ()
                  .put ("from", from)
                  .put ("message", message));
              } catch (JSONException e) {
                e.printStackTrace ();
              }
            }
          });
        }
      });
    } catch (Exception e) {
      e.printStackTrace ();
    }
  }
}

// client side
import android.os.Bundle;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ListView;
import androidx.appcompat.app.AppCompatActivity;
import io.socket.client.IO;
import io.socket.client.Socket;
import io.socket.emitter.Emitter;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

  private Socket socket; // socket instance variable
  private EditText editText; // input field for message
  private ImageButton sendButton; // button for sending message
  private ListView messagesView; // list view for displaying messages

  @Override
  protected void onCreate (Bundle savedInstanceState) {
    super.onCreate (savedInstanceState);
    setContentView (R.layout.activity_main);

    try {
      // create a socket connection to the server
      socket = IO.socket ("http://localhost");
      // connect to the server
      socket.connect ();
      // join a room with user id
      socket.emit ("join", new JSONObject ()
        .put ("userId", "user1"));
      // listen for receive events
      socket.on ("receive", new Emitter.Listener () {
        @Override
        public void call (Object... args) {
          try {
            // get the message data from the data
            JSONObject data = (JSONObject) args [0];
            String from = data.getString ("from");
            String message = data.getString ("message");
            // display the message on the list view
            runOnUiThread (() -> {
              messagesView.add (new MessageItem (from + ": " + message));
            });
          } catch (Exception e) {
            e.printStackTrace ();
          }
        }
      });
    } catch (Exception e) {
      e.printStackTrace ();
    }

    // get the views from the layout